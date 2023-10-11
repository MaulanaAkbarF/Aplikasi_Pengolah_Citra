const text = "Aplikasi Pengolah Citra dan Vision";
let charIndex = 0;

function type() {
  const element = document.getElementById("typerwriter-text");
  if (charIndex <= text.length) {
    element.textContent = text.slice(0, charIndex);
    charIndex++;
    setTimeout(type, 100); // Waktu jeda antar karakter (milidetik)
  }
}

// Jalankan animasi ketika dokumen dimuat
document.addEventListener("DOMContentLoaded", type);
