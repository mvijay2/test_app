
document.addEventListener("DOMContentLoaded", function () {
    function updateTotal() {
        let male = parseInt(document.getElementById("male_participants").value) || 0;
        let female = parseInt(document.getElementById("female_participants").value) || 0;
        document.getElementById("total_participants").value = male + female;
    }
    document.getElementById("male_participants").addEventListener("input", updateTotal);
    document.getElementById("female_participants").addEventListener("input", updateTotal);
});

// edit the event
document.addEventListener("DOMContentLoaded", function () {
    function updateTotal(event_id) {
        let male = parseInt(document.getElementById("male_participants_" + event_id).value) || 0;
        let female = parseInt(document.getElementById("female_participants_" + event_id).value) || 0;
        document.getElementById("total_participants_" + event_id).value = male + female;
    }
    document.querySelectorAll(".male_participants, .female_participants").forEach((element) => {
        element.addEventListener("input", function () {
            let event_id = this.id.split("_").pop();
            updateTotal(event_id);
        });
    });
});
