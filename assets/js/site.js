// Close the mobile navigation after selecting an in-page link.
document.querySelectorAll('#navbarResponsive a[href^="#"]').forEach(function (link) {
  link.addEventListener('click', function () {
    if (window.innerWidth < 992 && window.jQuery) {
      window.jQuery('#navbarResponsive').collapse('hide');
    }
  });
});
