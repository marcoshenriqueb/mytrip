import 'normalize.css';
import './../css/paraxify.css';
import './../styl/home.styl';

import './../js/paraxify';
import Shuffle from 'shufflejs';
import Inputmask from "inputmask";

document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener('scroll', () => {
        const scroll = document.body.scrollTop;
        if (scroll > 400) {
            document.querySelector('.header').classList.add('affix');
        } else {
            document.querySelector('.header').classList.remove('affix');
        }
    });

    document.getElementById('mobile-menu').addEventListener('click', () => {
        document.querySelector('header.header').classList.toggle('active');
    });

    // Adjusts cover video size
    const adjustVideo = () => {
        const w = window.innerWidth;
        if (w > 768 && top.offsetHeight > v.offsetHeight) {
            const vRatio = (v.videoHeight - 20) / v.videoWidth;
            top.style.height = (vRatio * w) + 'px';
        }
    }
    const top = document.querySelector('.top');
    const v = document.getElementsByTagName('video')[0];
    if (v) {
        v.addEventListener('loadeddata', () => {
            adjustVideo();
        });
    }

    // Parallax home page
    paraxify('.paraxify');

    // Clients testimonials
    let testPosition = 0;
    const moveTestimonials = (direction) => {
        const testContainer = document.getElementById('testimonial-container');
        const testCount = document.querySelectorAll('.testimonial-content').length;
        if (direction === 'right') {
            if (testPosition < testCount - 1) {
                const move = (testPosition + 1) * 100;
                testContainer.style.transform = `translateX(-${move}%)`;
                testPosition++;
            } else {
                testContainer.style.transform = 'translateX(0)';
                testPosition = 0;
            }
        } else {
            if (testPosition > 0) {
                const move = (testPosition - 1) * 100;
                testContainer.style.transform = `translateX(-${move}%)`;
                testPosition--;
            } else {
                const move = (testCount - 1) * 100;
                testContainer.style.transform = `translateX(-${move}%)`;
                testPosition = testCount - 1;
            }
        }
    };

    const startTestimonials = (el, direction) => {
        el.addEventListener('click', () => {
            moveTestimonials(direction);
        });
    };

    const arrowLeft = document.getElementById('testimonial-control-left');
    const arrowRight = document.getElementById('testimonial-control-right');
    if (arrowRight && arrowLeft) {
        startTestimonials(arrowLeft, 'left');
        startTestimonials(arrowRight, 'right');
        setInterval(() => {
            moveTestimonials('right');
        }, 8000);
    }

    const onResize = () => {
        if (v) {
            adjustVideo();
        }
    };
    window.onresize = onResize;

    Inputmask({ 'mask': '(99) [9]9999-9999' }).mask('.telephone-number');
    Inputmask({ 'mask': '99/99/9999' }).mask('.date-input');
});
