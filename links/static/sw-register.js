if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('/static/service-worker.js')
        .then(function(reg) {
          console.log('Service Worker registrado:', reg);
        })
        .catch(function(err) {
          console.log('Erro ao registrar o Service Worker:', err);
        });
    });
  }
  
  // Evento para capturar a instalação do PWA
  let installPromptEvent;
  
  window.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    installPromptEvent = event;
    document.getElementById('install-button').style.display = 'block';
  });
  
  document.getElementById('install-button').addEventListener('click', () => {
    if (installPromptEvent) {
      installPromptEvent.prompt();
      installPromptEvent.userChoice.then((choice) => {
        if (choice.outcome === 'accepted') {
          console.log('Usuário instalou o PWA');
        }
      });
    }
  });
  