const API_URL = window.location.origin; // Utilise l'URL actuelle (localhost:5000 ou production)

async function analyzeMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    
    // Validation
    if (!message) {
        showError('Veuillez entrer un message à analyser.');
        return;
    }
    
    // Afficher le loader
    const analyzeBtn = document.getElementById('analyzeBtn');
    const btnText = document.getElementById('btnText');
    const btnLoader = document.getElementById('btnLoader');
    
    analyzeBtn.disabled = true;
    btnText.classList.add('hidden');
    btnLoader.classList.remove('hidden');
    
    // Cacher les résultats précédents
    hideResults();
    hideError();
    
    try {
        // Appel API
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Erreur lors de l\'analyse');
        }
        
        const data = await response.json();
        displayResults(data);
        
    } catch (error) {
        console.error('Erreur:', error);
        showError(error.message || 'Erreur de connexion avec le serveur. Vérifiez que l\'API est lancée.');
    } finally {
        // Réactiver le bouton
        analyzeBtn.disabled = false;
        btnText.classList.remove('hidden');
        btnLoader.classList.add('hidden');
    }
}

function displayResults(data) {
    const resultSection = document.getElementById('resultSection');
    const resultTitle = document.getElementById('resultTitle');
    const resultBadge = document.getElementById('resultBadge');
    const spamPercent = document.getElementById('spamPercent');
    const hamPercent = document.getElementById('hamPercent');
    const spamBar = document.getElementById('spamBar');
    const hamBar = document.getElementById('hamBar');
    
    // Afficher la section
    resultSection.classList.remove('hidden');
    
    // Définir le résultat
    const isSpam = data.prediction === 'spam';
    resultTitle.textContent = isSpam ? '⚠️ Message suspect détecté !' : '✅ Message légitime';
    resultBadge.textContent = isSpam ? 'SPAM' : 'HAM';
    resultBadge.className = `badge ${isSpam ? 'spam' : 'ham'}`;
    
    // Afficher les pourcentages
    const spamConf = Math.round(data.confidence_spam);
    const hamConf = Math.round(data.confidence_ham);
    
    spamPercent.textContent = `${spamConf}%`;
    hamPercent.textContent = `${hamConf}%`;
    
    // Animer les barres de progression
    setTimeout(() => {
        spamBar.style.width = `${spamConf}%`;
        hamBar.style.width = `${hamConf}%`;
    }, 100);
}

function showError(message) {
    const errorSection = document.getElementById('errorSection');
    const errorMessage = document.getElementById('errorMessage');
    
    errorMessage.textContent = message;
    errorSection.classList.remove('hidden');
}

function hideError() {
    const errorSection = document.getElementById('errorSection');
    errorSection.classList.add('hidden');
}

function hideResults() {
    const resultSection = document.getElementById('resultSection');
    resultSection.classList.add('hidden');
}

// Permettre d'appuyer sur Entrée dans le textarea (Ctrl+Entrée pour envoyer)
document.getElementById('messageInput').addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.ctrlKey) {
        analyzeMessage();
    }
});

// Vérifier la connexion au serveur au chargement
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (!response.ok) {
            console.warn('Le serveur ne répond pas correctement');
        }
    } catch (error) {
        console.warn('Impossible de se connecter au serveur:', error);
    }
});
