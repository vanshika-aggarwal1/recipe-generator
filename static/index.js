async function generateRecipe() {
  const ingredients = document.getElementById("ingredients");
  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ingredients: ingredients }),
  });
  const data = await res.json();
  document.getElementById("recipe").innerText = data.recipe;
}