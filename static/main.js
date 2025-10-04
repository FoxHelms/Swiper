console.log("Sanity check!");

fetch("/config")
  .then((result) => {
    return result.json();
  })
  .then((data) => {
    const stripe = Stripe(data.publicKey);

    document.querySelector("#buyBtn").addEventListener("click", () => {
      // Get Checkout Session ID
      console.log(" You Click Button!");
      fetch("/create-checkout-session");
    });
  })
  .catch((err) => console.error("Failed to fetch config:", err));
