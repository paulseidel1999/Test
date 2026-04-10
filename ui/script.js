const button = document.getElementById('action-btn');
const status = document.getElementById('status-msg');
if (button) {
    button.addEventListener('click', () => {
        if (status) {
            status.textContent = 'Aktion erfolgreich ausgefuehrt.';
        }
        alert('Aktion ausgefuehrt!');
    });
}
