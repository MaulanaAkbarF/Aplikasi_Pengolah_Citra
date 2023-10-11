<script>
  const text = "Aplikasi Pengolah Citra dan Vision";
  let charIndex = 0;
  let timer;

  function type() {
    document.getElementById("typerwriter-text").textContent = text.slice(0, charIndex++);
    if (charIndex <= text.length) {
      timer = setTimeout(type, 100); // Waktu jeda antar karakter (milidetik)
    }
  }

  // Mulai animasi ketika halaman dimuat
  window.addEventListener("load", () => {
    type();
  });
</script>
