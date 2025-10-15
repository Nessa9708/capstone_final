const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const path = require("path");

const { Review } = require("./database/review");
const { Dealer } = require("./database/dealership");

const app = express();
app.use(cors());
app.use(express.json());

const mongoUrl = process.env.MONGO_URL || "mongodb://localhost:27017/dealershipsdb";

async function connect() {
  try {
    await mongoose.connect(mongoUrl, { useNewUrlParser: true, useUnifiedTopology: true });
    console.log("Connected to Mongo:", mongoUrl);

    // Seed data once if empty
    const reviewCount = await Review.countDocuments();
    const dealerCount = await Dealer.countDocuments();
    if (dealerCount === 0 || reviewCount === 0) {
      console.log("Seeding Mongo collections from JSON…");
      const reviews = require("./database/data/reviews.json");
      const dealers = require("./database/data/dealerships.json");
      if (dealerCount === 0) await Dealer.insertMany(dealers);
      if (reviewCount === 0) await Review.insertMany(reviews);
      console.log("Seeding complete.");
    }
  } catch (err) {
    console.error("Mongo connection error:", err);
  }
}
connect();

/** -------------------- ENDPOINTS -------------------- **/

// GET all reviews
app.get("/fetchReviews", async (req, res) => {
  const items = await Review.find({});
  res.json(items);
});

// GET reviews for a specific dealer id
app.get("/fetchReviews/dealer/:dealerId", async (req, res) => {
  const { dealerId } = req.params;
  const items = await Review.find({ dealerId: Number(dealerId) });
  res.json(items);
});

// GET all dealers
app.get("/fetchDealers", async (req, res) => {
  const items = await Dealer.find({});
  res.json(items);
});

// GET dealers by state
app.get("/fetchDealers/state/:state", async (req, res) => {
  const { state } = req.params;
  const items = await Dealer.find({ state });
  res.json(items);
});

// GET dealer by id
app.get("/fetchDealer/:id", async (req, res) => {
  const { id } = req.params;
  const item = await Dealer.findOne({ id: Number(id) });
  if (!item) return res.status(404).json({ error: "Dealer not found" });
  res.json(item);
});

// Simple health
app.get("/", (req, res) => res.send("Node app up"));

const PORT = process.env.PORT || 3030;
app.listen(PORT, () => console.log(`Node app listening on port ${PORT}`));
