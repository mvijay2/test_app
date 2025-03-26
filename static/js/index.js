window.addEventListener('load', () => {
    const track = document.querySelector('.carousel-track');
    const slides = Array.from(track.children);
    const nextButton = document.querySelector('.carousel-button.right');
    const prevButton = document.querySelector('.carousel-button.left');
  
    let slideWidth = slides[0].getBoundingClientRect().width;
  
    // Position slides next to each other
    // slides.forEach((slide, index) => {
    //   slide.style.left = slideWidth * index + 'px';
    // });
  
    let currentSlideIndex = 0;
  
    function moveToSlide(index) {
      track.style.transform = `translateX(-${slideWidth * index}px)`;
      currentSlideIndex = index;
    }
  
    nextButton.addEventListener('click', () => {
      let nextIndex = (currentSlideIndex + 1) % slides.length;
      moveToSlide(nextIndex);
    });
  
    prevButton.addEventListener('click', () => {
      let prevIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
      moveToSlide(prevIndex);
    });
  
    // Handle window resize
    window.addEventListener('resize', () => {
      slideWidth = slides[0].getBoundingClientRect().width;
  
      slides.forEach((slide, index) => {
        slide.style.left = slideWidth * index + 'px';
      });
  
      moveToSlide(currentSlideIndex);
    });
  
    // Optional: Auto-slide every 5 seconds
    setInterval(() => {
      let nextIndex = (currentSlideIndex + 1) % slides.length;
      moveToSlide(nextIndex);
    }, 5000);
  });
  