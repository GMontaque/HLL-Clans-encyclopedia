// sets status of notification

let notification_status = document.getElementsByClassName("status-icon");

for (let i = 0; i < notification_status.length; i++) {
	statusVal = notification_status[i].textContent.trim();
	statusVal = statusVal.charAt(0).toUpperCase() + statusVal.slice(1);
	let icon = "";
	if (statusVal == "Completed") {
		icon = '<i class="fa-solid fa-circle-check fa-2xl"></i>';
	} else if (statusVal == "Rejected") {
		icon = '<i class="fa-solid fa-circle-xmark fa-2xl"></i>';
	} else {
		icon = '<i class="fa-solid fa-clock fa-2xl"></i>';
	}
	notification_status[i].innerHTML = icon + " " + statusVal;
}
