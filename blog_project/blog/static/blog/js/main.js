// Javascript for Django Project

// Function to allow dropdown upon clicking an anchor tag

$('ul.nav li.dropdown').hover(
	function() {
		$(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
	}, 
	function() {
		$(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
	}
);
