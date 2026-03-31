// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// Scroll Reveal Animation using IntersectionObserver
const revealElements = document.querySelectorAll('.reveal');

const revealCallback = function (entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            // Unobserve if you only want the animation to play once
            // observer.unobserve(entry.target);
        }
    });
};

const revealOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
};

const revealObserver = new IntersectionObserver(revealCallback, revealOptions);

revealElements.forEach(el => {
    revealObserver.observe(el);
});

// Form submission handler (mock with loading effect)
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = contactForm.querySelector('button');
        const originalText = btn.textContent;

        btn.textContent = 'Sending...';
        btn.disabled = true;

        // Mock API call delay
        setTimeout(() => {
            btn.textContent = 'Message Sent!';
            contactForm.reset();

            setTimeout(() => {
                btn.textContent = originalText;
                btn.disabled = false;
            }, 3000);
        }, 1500);
    });
}

// Typing Effect
const typedWords = ["Data Science", "AI/ML", "Machine Learning", "Deep Learning"];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typingElement = document.querySelector(".typing-text");

function typeEffect() {
    if (!typingElement) return;

    const currentWord = typedWords[wordIndex];

    if (isDeleting) {
        typingElement.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typingElement.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
    }

    let typeSpeed = isDeleting ? 40 : 100;

    if (!isDeleting && charIndex === currentWord.length) {
        typeSpeed = 2000; // Pause at end of word
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % typedWords.length;
        typeSpeed = 400; // Pause before next word
    }

    setTimeout(typeEffect, typeSpeed);
}

// Start typing effect
setTimeout(typeEffect, 1000);

// Gallery Modal Logic
const galleryBtns = document.querySelectorAll('.gallery-btn');
const modalOverlay = document.getElementById('gallery-modal');
const closeModal = document.getElementById('close-modal');
const modalTrack = document.getElementById('modal-track');
const modalNav = document.getElementById('modal-nav');
const modalPrev = document.getElementById('modal-prev');
const modalNext = document.getElementById('modal-next');
let modalCurrentIndex = 0;
let modalSlides = [];
let modalDots = [];

const updateModalCarousel = (index) => {
    modalTrack.style.transform = 'translateX(-' + (index * 100) + '%)';
    modalDots.forEach(dot => dot.classList.remove('current-slide'));
    if(modalDots[index]) modalDots[index].classList.add('current-slide');
};

galleryBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const imagesStr = btn.getAttribute('data-images');
        if(!imagesStr) return;
        
        const images = imagesStr.split(',');
        
        // Clear existing
        modalTrack.innerHTML = '';
        modalNav.innerHTML = '';
        modalSlides = [];
        modalDots = [];
        modalCurrentIndex = 0;
        
        // Populate
        images.forEach((imgSrc, i) => {
            const img = document.createElement('img');
            img.src = imgSrc;
            img.className = 'carousel-slide';
            img.style.objectFit = 'contain';
            img.style.width = '100%';
            img.style.flexShrink = '0';
            modalTrack.appendChild(img);
            modalSlides.push(img);
            
            const dot = document.createElement('button');
            dot.className = 'carousel-indicator';
            if(i === 0) dot.classList.add('current-slide');
            dot.addEventListener('click', () => {
                modalCurrentIndex = i;
                updateModalCarousel(modalCurrentIndex);
            });
            modalNav.appendChild(dot);
            modalDots.push(dot);
        });
        
        updateModalCarousel(0);
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // prevent scrolling behind
    });
});

closeModal.addEventListener('click', () => {
    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
});

modalOverlay.addEventListener('click', (e) => {
    if(e.target === modalOverlay) {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }
});

if(modalNext) {
    modalNext.addEventListener('click', () => {
        if(modalSlides.length <= 1) return;
        modalCurrentIndex = (modalCurrentIndex === modalSlides.length - 1) ? 0 : modalCurrentIndex + 1;
        updateModalCarousel(modalCurrentIndex);
    });
}

if(modalPrev) {
    modalPrev.addEventListener('click', () => {
        if(modalSlides.length <= 1) return;
        modalCurrentIndex = (modalCurrentIndex === 0) ? modalSlides.length - 1 : modalCurrentIndex - 1;
        updateModalCarousel(modalCurrentIndex);
    });
}

// Background Spark Particles
const canvas = document.getElementById('spark-canvas');
if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;
    const particles = [];

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            // Soft random movement
            this.vx = (Math.random() - 0.5) * 1;
            this.vy = (Math.random() - 0.5) * 1 - 0.5; // Slight upward drift
            this.size = Math.random() * 2 + 1;
            this.alpha = Math.random() * 0.5 + 0.3;
            // Match the accent colors of the site to feel continuous
            this.color = Math.random() > 0.5 ? '#8b5cf6' : '#0ea5e9';
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            // Wrap around edges smoothly
            if (this.x < 0) this.x = width;
            if (this.x > width) this.x = 0;
            if (this.y < 0) this.y = height;
            if (this.y > height) this.y = 0;
        }
        draw() {
            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    for (let i = 0; i < 70; i++) {
        particles.push(new Particle());
    }

    function animateSparks() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {
            p.update();
            p.draw();
        });
        requestAnimationFrame(animateSparks);
    }
    animateSparks();
}
