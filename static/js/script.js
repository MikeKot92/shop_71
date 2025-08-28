// SportShop JavaScript Functions

// document.addEventListener('DOMContentLoaded', function() {
//     // Initialize all components
//     initializeCart();
//     initializeProductFilters();
//     initializeSearch();
//     initializeQuantityControls();
//     initializeWishlist();
//     initializeNotifications();
// });

// Функция для показа и скрытия сообщения
document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popupMessage");

    // Показываем сообщение
    popup.classList.add("show");

    // Скрываем сообщение через 5 секунд
    setTimeout(() => {
        popup.classList.remove("show");

        // Удаляем сообщение из DOM после завершения анимации
        setTimeout(() => {
            popup.remove();
        }, 300); // 300ms — время анимации исчезновения
    }, 3000); // 3000ms = 3 секунд
});

// // Cart Management
// let cart = JSON.parse(localStorage.getItem('sportshop_cart')) || [];
//
// // function initializeCart() {
// //     updateCartBadge();
// //
// //     // Add to cart buttons
// //     document.querySelectorAll('.btn:contains("В корзину")').forEach(button => {
// //         button.addEventListener('click', function(e) {
// //             e.preventDefault();
// //             const productCard = this.closest('.product-card');
// //             addToCart(productCard);
// //         });
// //     });
// // }
//
// function addToCart(productElement) {
//     const product = {
//         id: Date.now(),
//         name: productElement.querySelector('.card-title').textContent,
//         price: extractPrice(productElement.querySelector('.text-primary').textContent),
//         image: productElement.querySelector('img').src,
//         quantity: 1
//     };
//
//     const existingItem = cart.find(item => item.name === product.name);
//
//     if (existingItem) {
//         existingItem.quantity += 1;
//     } else {
//         cart.push(product);
//     }
//
//     localStorage.setItem('sportshop_cart', JSON.stringify(cart));
//     updateCartBadge();
//     showNotification('Товар добавлен в корзину!', 'success');
// }
//
// function removeFromCart(productId) {
//     cart = cart.filter(item => item.id !== productId);
//     localStorage.setItem('sportshop_cart', JSON.stringify(cart));
//     updateCartBadge();
//     updateCartPage();
//     showNotification('Товар удален из корзины', 'info');
// }
//
// function updateQuantity(productId, newQuantity) {
//     const item = cart.find(item => item.id === productId);
//     if (item) {
//         item.quantity = Math.max(1, newQuantity);
//         localStorage.setItem('sportshop_cart', JSON.stringify(cart));
//         updateCartBadge();
//         updateCartPage();
//     }
// }
//
// function updateCartBadge() {
//     const badge = document.querySelector('.badge');
//     if (badge) {
//         const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
//         badge.textContent = totalItems;
//         badge.style.display = totalItems > 0 ? 'block' : 'none';
//     }
// }
//
// function updateCartPage() {
//     // Update cart page if we're on it
//     if (window.location.pathname.includes('cart.html')) {
//         renderCartItems();
//         updateOrderSummary();
//     }
// }
//
// function renderCartItems() {
//     const cartContainer = document.querySelector('.cart-items');
//     if (!cartContainer) return;
//
//     if (cart.length === 0) {
//         cartContainer.innerHTML = `
//             <div class="text-center py-5">
//                 <i class="fas fa-shopping-cart fa-3x text-muted mb-3"></i>
//                 <h4>Корзина пуста</h4>
//                 <p class="text-muted">Добавьте товары из каталога</p>
//                 <a href="catalog.html" class="btn btn-primary">Перейти в каталог</a>
//             </div>
//         `;
//         return;
//     }
//
//     cartContainer.innerHTML = cart.map(item => `
//         <div class="row align-items-center border-bottom py-3 cart-item" data-id="${item.id}">
//             <div class="col-md-2">
//                 <img src="${item.image}" class="img-fluid rounded" alt="${item.name}">
//             </div>
//             <div class="col-md-4">
//                 <h6 class="mb-1">${item.name}</h6>
//                 <small class="text-muted">Артикул: ${generateSKU(item.name)}</small>
//                 <div class="mt-2">
//                     <span class="badge bg-success">В наличии</span>
//                 </div>
//             </div>
//             <div class="col-md-2">
//                 <div class="input-group input-group-sm">
//                     <button class="btn btn-outline-secondary quantity-btn" data-action="decrease">-</button>
//                     <input type="text" class="form-control text-center quantity-input" value="${item.quantity}">
//                     <button class="btn btn-outline-secondary quantity-btn" data-action="increase">+</button>
//                 </div>
//             </div>
//             <div class="col-md-2 text-center">
//                 <div class="fw-bold text-primary">${formatPrice(item.price)}₽</div>
//             </div>
//             <div class="col-md-2 text-end">
//                 <button class="btn btn-outline-danger btn-sm remove-item">
//                     <i class="fas fa-trash"></i>
//                 </button>
//             </div>
//         </div>
//     `).join('');
// }
//
// function updateOrderSummary() {
//     const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
//     const discount = subtotal > 5000 ? 1000 : 0;
//     const shipping = subtotal > 5000 ? 0 : 500;
//     const total = subtotal - discount + shipping;
//
//     const summaryElement = document.querySelector('.order-summary');
//     if (summaryElement) {
//         summaryElement.innerHTML = `
//             <div class="d-flex justify-content-between mb-2">
//                 <span>Товары (${cart.reduce((sum, item) => sum + item.quantity, 0)} шт.):</span>
//                 <span>${formatPrice(subtotal)}₽</span>
//             </div>
//             <div class="d-flex justify-content-between mb-2">
//                 <span>Скидка:</span>
//                 <span class="text-success">-${formatPrice(discount)}₽</span>
//             </div>
//             <div class="d-flex justify-content-between mb-2">
//                 <span>Доставка:</span>
//                 <span class="${shipping === 0 ? 'text-success' : ''}">${shipping === 0 ? 'Бесплатно' : formatPrice(shipping) + '₽'}</span>
//             </div>
//             <hr>
//             <div class="d-flex justify-content-between mb-3">
//                 <strong>Итого:</strong>
//                 <strong class="text-primary">${formatPrice(total)}₽</strong>
//             </div>
//         `;
//     }
// }
//
// // Product Filters
// function initializeProductFilters() {
//     const filterCheckboxes = document.querySelectorAll('.form-check-input');
//     const sortSelect = document.querySelector('select');
//
//     filterCheckboxes.forEach(checkbox => {
//         checkbox.addEventListener('change', applyFilters);
//     });
//
//     if (sortSelect) {
//         sortSelect.addEventListener('change', applySorting);
//     }
// }
//
// function applyFilters() {
//     const activeFilters = {
//         categories: [],
//         brands: [],
//         priceRange: { min: 0, max: Infinity },
//         rating: 0
//     };
//
//     // Collect active filters
//     document.querySelectorAll('.form-check-input:checked').forEach(checkbox => {
//         const filterType = checkbox.closest('.mb-4').querySelector('h6').textContent;
//         const filterValue = checkbox.nextElementSibling.textContent.trim();
//
//         if (filterType === 'Категории') {
//             activeFilters.categories.push(filterValue.split(' ')[0]);
//         } else if (filterType === 'Бренд') {
//             activeFilters.brands.push(filterValue);
//         }
//     });
//
//     filterProducts(activeFilters);
// }
//
// function filterProducts(filters) {
//     const products = document.querySelectorAll('.product-card');
//     let visibleCount = 0;
//
//     products.forEach(product => {
//         let shouldShow = true;
//
//         // Apply category filter
//         if (filters.categories.length > 0) {
//             // Implementation would depend on product data structure
//         }
//
//         // Apply brand filter
//         if (filters.brands.length > 0) {
//             // Implementation would depend on product data structure
//         }
//
//         // Apply price filter
//         const priceElement = product.querySelector('.text-primary');
//         if (priceElement) {
//             const price = extractPrice(priceElement.textContent);
//             if (price < filters.priceRange.min || price > filters.priceRange.max) {
//                 shouldShow = false;
//             }
//         }
//
//         product.closest('.col-lg-4, .col-lg-3, .col-md-6').style.display = shouldShow ? 'block' : 'none';
//         if (shouldShow) visibleCount++;
//     });
//
//     updateProductCount(visibleCount);
// }
//
// function applySorting() {
//     const sortValue = event.target.value;
//     const productsContainer = document.querySelector('#products-grid');
//     const products = Array.from(productsContainer.children);
//
//     products.sort((a, b) => {
//         switch (sortValue) {
//             case 'По цене (возрастание)':
//                 return extractPrice(a.querySelector('.text-primary').textContent) -
//                        extractPrice(b.querySelector('.text-primary').textContent);
//             case 'По цене (убывание)':
//                 return extractPrice(b.querySelector('.text-primary').textContent) -
//                        extractPrice(a.querySelector('.text-primary').textContent);
//             case 'По рейтингу':
//                 return getRating(b) - getRating(a);
//             default:
//                 return 0;
//         }
//     });
//
//     products.forEach(product => productsContainer.appendChild(product));
// }
//
// // Search Functionality
// function initializeSearch() {
//     const searchInput = document.querySelector('input[type="search"]');
//     if (searchInput) {
//         searchInput.addEventListener('input', debounce(performSearch, 300));
//     }
// }
//
// function performSearch() {
//     const query = event.target.value.toLowerCase();
//     const products = document.querySelectorAll('.product-card');
//
//     products.forEach(product => {
//         const title = product.querySelector('.card-title').textContent.toLowerCase();
//         const description = product.querySelector('.card-text').textContent.toLowerCase();
//         const matches = title.includes(query) || description.includes(query);
//
//         product.closest('.col-lg-4, .col-lg-3, .col-md-6').style.display = matches ? 'block' : 'none';
//     });
// }
//
// // Quantity Controls
// function initializeQuantityControls() {
//     document.addEventListener('click', function(e) {
//         if (e.target.classList.contains('quantity-btn')) {
//             const action = e.target.dataset.action;
//             const input = e.target.parentElement.querySelector('.quantity-input');
//             const currentValue = parseInt(input.value);
//
//             if (action === 'increase') {
//                 input.value = currentValue + 1;
//             } else if (action === 'decrease' && currentValue > 1) {
//                 input.value = currentValue - 1;
//             }
//
//             // Update cart if on cart page
//             const cartItem = e.target.closest('.cart-item');
//             if (cartItem) {
//                 const productId = parseInt(cartItem.dataset.id);
//                 updateQuantity(productId, parseInt(input.value));
//             }
//         }
//
//         if (e.target.classList.contains('remove-item')) {
//             const cartItem = e.target.closest('.cart-item');
//             if (cartItem) {
//                 const productId = parseInt(cartItem.dataset.id);
//                 removeFromCart(productId);
//             }
//         }
//     });
// }
//
// // Wishlist Functionality
// let wishlist = JSON.parse(localStorage.getItem('sportshop_wishlist')) || [];
//
// function initializeWishlist() {
//     document.addEventListener('click', function(e) {
//         if (e.target.classList.contains('fa-heart')) {
//             toggleWishlist(e.target.closest('.product-card'));
//         }
//     });
// }
//
// function toggleWishlist(productElement) {
//     const productName = productElement.querySelector('.card-title').textContent;
//     const index = wishlist.findIndex(item => item.name === productName);
//
//     if (index > -1) {
//         wishlist.splice(index, 1);
//         showNotification('Товар удален из избранного', 'info');
//     } else {
//         const product = {
//             name: productName,
//             price: extractPrice(productElement.querySelector('.text-primary').textContent),
//             image: productElement.querySelector('img').src
//         };
//         wishlist.push(product);
//         showNotification('Товар добавлен в избранное!', 'success');
//     }
//
//     localStorage.setItem('sportshop_wishlist', JSON.stringify(wishlist));
// }
//
// // Notifications
// function initializeNotifications() {
//     // Create notification container if it doesn't exist
//     if (!document.querySelector('.notification-container')) {
//         const container = document.createElement('div');
//         container.className = 'notification-container';
//         container.style.cssText = `
//             position: fixed;
//             top: 20px;
//             right: 20px;
//             z-index: 1050;
//             max-width: 300px;
//         `;
//         document.body.appendChild(container);
//     }
// }
//
// function showNotification(message, type = 'info') {
//     const container = document.querySelector('.notification-container');
//     const notification = document.createElement('div');
//
//     const typeClasses = {
//         success: 'alert-success',
//         error: 'alert-danger',
//         warning: 'alert-warning',
//         info: 'alert-info'
//     };
//
//     notification.className = `alert ${typeClasses[type]} alert-dismissible fade show`;
//     notification.innerHTML = `
//         ${message}
//         <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
//     `;
//
//     container.appendChild(notification);
//
//     // Auto remove after 3 seconds
//     setTimeout(() => {
//         if (notification.parentElement) {
//             notification.remove();
//         }
//     }, 3000);
// }
//
// // Utility Functions
// function extractPrice(priceText) {
//     return parseInt(priceText.replace(/[^\d]/g, ''));
// }
//
// function formatPrice(price) {
//     return price.toLocaleString('ru-RU');
// }
//
// function getRating(productElement) {
//     const stars = productElement.querySelectorAll('.fas.fa-star');
//     return stars.length;
// }
//
// function generateSKU(productName) {
//     return productName.split(' ').map(word => word.substring(0, 2).toUpperCase()).join('-') + '-001';
// }
//
// function updateProductCount(count) {
//     const countElement = document.querySelector('.text-muted');
//     if (countElement && countElement.textContent.includes('Найдено товаров:')) {
//         countElement.textContent = `Найдено товаров: ${count}`;
//     }
// }
//
// function debounce(func, wait) {
//     let timeout;
//     return function executedFunction(...args) {
//         const later = () => {
//             clearTimeout(timeout);
//             func(...args);
//         };
//         clearTimeout(timeout);
//         timeout = setTimeout(later, wait);
//     };
// }
//
// // Smooth scrolling for anchor links
// document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//     anchor.addEventListener('click', function (e) {
//         e.preventDefault();
//         const target = document.querySelector(this.getAttribute('href'));
//         if (target) {
//             target.scrollIntoView({
//                 behavior: 'smooth',
//                 block: 'start'
//             });
//         }
//     });
// });
//
// // Form validation
// function validateForm(form) {
//     const inputs = form.querySelectorAll('input[required]');
//     let isValid = true;
//
//     inputs.forEach(input => {
//         if (!input.value.trim()) {
//             input.classList.add('is-invalid');
//             isValid = false;
//         } else {
//             input.classList.remove('is-invalid');
//         }
//     });
//
//     return isValid;
// }
//
// // Newsletter subscription
// document.addEventListener('submit', function(e) {
//     if (e.target.closest('form') && e.target.querySelector('input[type="email"]')) {
//         e.preventDefault();
//         const email = e.target.querySelector('input[type="email"]').value;
//
//         if (email) {
//             showNotification('Спасибо за подписку!', 'success');
//             e.target.reset();
//         }
//     }
// });
//
// // Lazy loading for images
// if ('IntersectionObserver' in window) {
//     const imageObserver = new IntersectionObserver((entries, observer) => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting) {
//                 const img = entry.target;
//                 img.src = img.dataset.src;
//                 img.classList.remove('lazy');
//                 imageObserver.unobserve(img);
//             }
//         });
//     });
//
//     document.querySelectorAll('img[data-src]').forEach(img => {
//         imageObserver.observe(img);
//     });
// }

