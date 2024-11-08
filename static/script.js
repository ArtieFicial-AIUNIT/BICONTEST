document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.getElementById('country');
    const conditionsDisplay = document.getElementById('conditions-display');
    const biconUrl = document.getElementById('bicon-url');

    // Remove the JSON.parse line since we now have the data from the template
    // const conditions = JSON.parse('{{ countries | tojson | safe }}');

    function updateConditions() {
        const selectedCountry = countrySelect.value;
        const countryData = importConditions[selectedCountry];
        
        if (countryData) {
            let html = `
                <h2><i class="fas fa-clipboard-list"></i> ${selectedCountry} Import Conditions</h2>
                <ul>
            `;
            countryData.conditions.forEach(condition => {
                html += `<li>${condition}</li>`;
            });
            html += '</ul>';
            
            // Fade effect
            conditionsDisplay.style.opacity = '0';
            setTimeout(() => {
                conditionsDisplay.innerHTML = html;
                conditionsDisplay.style.opacity = '1';
            }, 200);
            
            biconUrl.href = countryData.url;
        }
    }

    countrySelect.addEventListener('change', updateConditions);
    updateConditions(); // Initial load
});
