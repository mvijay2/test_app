let map;
const currentLayers = {};

document.addEventListener("DOMContentLoaded", () => {
  map = L.map('map').setView([20.5937, 78.9629], 5);

  L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
  }).addTo(map);

  const sidebar = document.getElementById("sidebar");
  const restoreBtn = document.getElementById("restoreSidebar");
  const toggleBtn = document.getElementById("toggleBtn");
  const minimizeBtn = document.getElementById("minimizeBtn");
  const checkboxContainer = document.getElementById("mapCheckboxList");

  toggleBtn.addEventListener("click", () => {
    checkboxContainer.style.display = checkboxContainer.style.display === 'none' ? 'block' : 'none';
  });

  minimizeBtn.addEventListener("click", () => {
    sidebar.classList.add("minimized");
    restoreBtn.style.display = "block";
  });

  restoreBtn.addEventListener("click", () => {
    sidebar.classList.remove("minimized");
    restoreBtn.style.display = "none";
  });

  fetch("/community/getmaps")
    .then(res => res.json())
    .then(maps => {
      maps.forEach(mapObj => {
        const label = document.createElement("label");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.value = mapObj.url;
        checkbox.dataset.name = mapObj.name;

        checkbox.addEventListener("change", async function () {
          const name = this.dataset.name;
          if (this.checked) {
            try {
              const res = await fetch(this.value);
              const geoData = await res.json();
              const layer = L.geoJSON(geoData, {
                onEachFeature: (feature, layer) => {
                  if (feature.properties?.name) {
                    layer.bindPopup("Name: " + feature.properties.name);
                  }
                },
                style: { color: "#3388ff", weight: 2 }
              }).addTo(map);
              currentLayers[name] = layer;
              map.fitBounds(layer.getBounds());
            } catch (err) {
              console.error("Failed to load", name, err);
            }
          } else {
            if (currentLayers[name]) {
              map.removeLayer(currentLayers[name]);
              delete currentLayers[name];
            }
          }
        });

        label.appendChild(checkbox);
        label.append(" " + mapObj.name);
        checkboxContainer.appendChild(label);
      });
    });
});
