document.addEventListener('DOMContentLoaded', function() {
  const display = document.getElementById('display');
  const kalkulatorContainer = document.getElementById('kalkulator-container');

  let errorState = false; // dodajemo flag za stanje greške

  if (kalkulatorContainer) {
    kalkulatorContainer.style.backgroundColor = 'lightblue';
  }

  function dodajNaDisplay(sadrzaj) {
    if (display.innerText.trim() === '0' || errorState) {
      display.innerText = sadrzaj;
      errorState = false; // resetiraj stanje greške ako dodajemo nešto novo
    } else {
      display.innerText += sadrzaj;
    }
  }

  document.querySelectorAll('.broj').forEach(btn => {
    btn.addEventListener('click', function() {
      const value = this.getAttribute('data-value');
      dodajNaDisplay(value);
    });
  });

  document.querySelectorAll('.operator').forEach(btn => {
    btn.addEventListener('click', function() {
      const op = this.getAttribute('data-op');
      dodajNaDisplay(op);
    });
  });

  document.getElementById('decimal').addEventListener('click', function() {
    dodajNaDisplay('.');
  });

  document.getElementById('clear').addEventListener('click', function() {
    display.innerText = '0';
    errorState = false;
  });

  document.getElementById('equals').addEventListener('click', function() {
    if (errorState) {
      // Ako smo u error stanju, ne evaluiraj, već resetiraj
      display.innerText = '0';
      errorState = false;
      return;
    }
    try {
      const izraz = display.innerText;
      const rezultat = eval(izraz);
      display.innerText = rezultat;
    } catch (e) {
      display.innerText = 'Error';
      errorState = true; // postavimo flag da smo u error stanju
    }
  });
});