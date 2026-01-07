/* ---------- GLOBAL STATE ---------- */
let cart = [];
let subTotal = 0;
let discountedTotal = 0;
let totalWithTax = 0;
let finalAmount = 0;
let invoiceData = {};

/* ---------- LAB 1: ADD ITEMS (WITH VALIDATION) ---------- */
function addItems() {
  cart = [];
  subTotal = 0;

  document.getElementById("output").innerHTML = "";

  while (true) {
    try {
      let itemCode = prompt("Item code:");
      let description = prompt("Item Description:");
      let quantity = Number(prompt("Quantity:"));
      let price = Number(prompt("Price per unit:"));

      if (
        !itemCode ||
        quantity <= 0 ||
        price <= 0 ||
        isNaN(quantity) ||
        isNaN(price)
      ) {
        throw new Error("Invalid item details entered");
      }

      let itemTotal = quantity * price;

      cart.push({
        itemCode,
        description,
        quantity,
        price,
        itemTotal
      });

      subTotal += itemTotal;

      if (prompt("Add another item? (yes/no)").toLowerCase() !== "yes") break;

    } catch (e) {
      display("Error (Lab 1): " + e.message);
    }
  }

  display("Subtotal (Lab 1 complete): ₹" + subTotal);
}

/* ---------- LAB 2: MEMBERSHIP DISCOUNT (VALIDATION) ---------- */
function applyDiscount() {
  if (subTotal === 0) {
    display("Error: Add items before discount");
    return;
  }

  let membership = prompt("Membership (None/Silver/Gold/Platinum):");
  let rate = 0;

  if (membership.toLowerCase === "silver") rate = 0.05;
  else if (membership.toLowerCase === "gold") rate = 0.10;
  else if (membership.toLowerCase === "platinum") rate = 0.15;
  else if (membership !== "None") {
    display("Invalid membership type");
    return;
  }

  discountedTotal = subTotal - (subTotal * rate);
  display("After Discount (Lab 2): ₹" + discountedTotal);
}

/* ---------- LAB 3: GST & PLATFORM FEE ---------- */
function addTax() {
  if (discountedTotal === 0) {
    display("Error: Apply discount before tax");
    return;
  }

  let gst = discountedTotal * 0.18;
  let fee = discountedTotal * 0.002;

  totalWithTax = discountedTotal + gst + fee;
  display("Total with GST & Platform Fee (Lab 3): ₹" + totalWithTax);
}

/* ---------- LAB 4: PAYMENT MODE (VALIDATION) ---------- */
function payment() {
  if (totalWithTax === 0) {
    display("Error: Calculate tax before payment");
    return;
  }

  let mode = prompt("Payment Mode (Card/UPI/Cash):");

  if (!["Card", "UPI", "Cash"].includes(mode)) {
    display("Invalid payment mode");
    return;
  }

  let extra =
    (mode.toLowerCase() === "card" && totalWithTax < 1000)
      ? totalWithTax * 0.025
      : totalWithTax * 0.01;

  finalAmount = totalWithTax + extra;
  display("Final Payable Amount (Lab 4): ₹" + finalAmount);
}

/* ---------- LAB 5: GENERATE INVOICE ---------- */
function generateInvoice() {
  if (finalAmount === 0) {
    display("Error: Complete payment before invoice");
    return;
  }

  invoiceData = {
    invoiceNo: "INV" + Math.floor(Math.random() * 10000),
    date: new Date().toLocaleString(),
    cart,
    finalAmount
  };

  display("Invoice Generated (Lab 5)");
  display("<pre>" + JSON.stringify(invoiceData, null, 2) + "</pre>");
}

/* ---------- LAB 6 & 8: EMAIL VALIDATION ---------- */
function sendEmail() {
  let email = prompt("Enter email:");
  let emailRegex = /^[\w.-]+@karunya\.edu$/;

  if (!emailRegex.test(email)) {
    display("Invalid email format or domain");
    return;
  }

  display("Invoice sent successfully to " + email);
}

/* ---------- LAB 7: LOCAL STORAGE ---------- */
function saveData() {
  if (cart.length === 0) {
    display("Nothing to save");
    return;
  }

  localStorage.setItem("cart", JSON.stringify(cart));
  localStorage.setItem("invoice", JSON.stringify(invoiceData));

  display("Cart & Invoice saved locally (Lab 7)");
}

/* ---------- LAB 10: CLOSURES ---------- */
function getDiscountFunction(type) {
  let rate = type === "Gold" ? 0.10 : 0.05;
  return function (amount) {
    return amount - (amount * rate);
  };
}

function closureDiscount() {
  let discountFn = getDiscountFunction("Gold");
  display("Closure Discount Result (Lab 10): ₹" + discountFn(subTotal));
}

/* ---------- LAB 11: ASYNC PAYMENT ---------- */
async function processPaymentAsync() {
  display("Processing payment... (Lab 11)");
  await new Promise(resolve => setTimeout(resolve, 2000));
  display("Payment Successful (Async)");
}

/* ---------- LAB 12: PROMISE INVENTORY ---------- */
function inventoryLookup() {
  return new Promise((resolve, reject) => {
    let stock = 3;
    stock > 0 ? resolve("Item In Stock") : reject("Out of Stock");
  });
}

function checkInventory() {
  inventoryLookup()
    .then(msg => display(msg + " (Lab 12)"))
    .catch(err => display(err + " (Lab 12)"));
}

/* ---------- LAB 13: CALLBACK ---------- */
function completeBilling(callback) {
  callback(invoiceData);
}

function callbackFn() {
  display("Billing completed. Thank you! (Lab 13)");
}

/* ---------- UTILITY: CONTINUOUS DISPLAY ---------- */
function display(msg) {
  document.getElementById("output").innerHTML += "<br>" + msg;
}
