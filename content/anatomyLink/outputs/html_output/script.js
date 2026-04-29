// AnatomyLink Interactive Features

document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchBox = document.getElementById('search-box');
    if (searchBox) {
        searchBox.addEventListener('input', debounce(handleSearch, 300));
    }

    // Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Highlight current page in navigation
    highlightCurrentPage();
});

function handleSearch(e) {
    const query = e.target.value.toLowerCase();
    if (query.length < 2) return;

    // This could be extended to search the content
    console.log('Search:', query);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function highlightCurrentPage() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('a[href]').forEach(link => {
        if (link.getAttribute('href').endsWith(currentPage)) {
            link.classList.add('active');
        }
    });
}
