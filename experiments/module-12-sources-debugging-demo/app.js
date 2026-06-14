'use strict';

const form = document.getElementById('pricing-form');
const resetButton = document.getElementById('reset-demo');
const statusNode = document.getElementById('status');
const subtotalNode = document.getElementById('subtotal');
const discountNode = document.getElementById('discount-amount');
const totalNode = document.getElementById('final-total');
const priceInput = document.getElementById('price');
const quantityInput = document.getElementById('quantity');
const discountInput = document.getElementById('discount');

function formatCurrency(value) {
  return value.toLocaleString('en-US', { maximumFractionDigits: 0 });
}

function readFormValues() {
  const price = Number(priceInput.value);
  const quantity = Number(quantityInput.value);
  const discountPercent = Number(discountInput.value);

  return {
    price,
    quantity,
    discountPercent,
  };
}

function calculateSubtotal(price, quantity) {
  return price * quantity;
}

function calculateDiscountAmount(subtotal, discountPercent) {
  // Fixed in Module 12-E: percentage calculation now divides by 100.
  return subtotal * (discountPercent / 100);
}

function calculateFinalTotal(subtotal, discountAmount) {
  return subtotal - discountAmount;
}

function renderResults(subtotal, discountAmount, finalTotal) {
  subtotalNode.textContent = formatCurrency(subtotal);
  discountNode.textContent = formatCurrency(discountAmount);
  totalNode.textContent = formatCurrency(finalTotal);
}

function updateStatus(message) {
  statusNode.textContent = message;
}

function runCalculation() {
  const { price, quantity, discountPercent } = readFormValues();
  const subtotal = calculateSubtotal(price, quantity);
  const discountAmount = calculateDiscountAmount(subtotal, discountPercent);
  const finalTotal = calculateFinalTotal(subtotal, discountAmount);

  renderResults(subtotal, discountAmount, finalTotal);
  updateStatus(
    `Calculated with price=${price}, quantity=${quantity}, discount=${discountPercent}%.`,
  );

  console.log('Module 12 demo calculation complete', {
    price,
    quantity,
    discountPercent,
    subtotal,
    discountAmount,
    finalTotal,
  });

  return {
    subtotal,
    discountAmount,
    finalTotal,
  };
}

function resetDemo() {
  priceInput.value = '100';
  quantityInput.value = '2';
  discountInput.value = '10';
  renderResults('-', '-', '-');
  updateStatus('Reset to the sample values. Ready for local debugging.');
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  runCalculation();
});

resetButton.addEventListener('click', () => {
  resetDemo();
});

resetDemo();
