import range from "./range_function.js";
let mainContainer = document.querySelector(".container");

function getDate(date) {
    return `${d.getDate()}/${d.getMonth()}/${d.getFullYear()}`;
}

const d = new Date(2021, 10, 27);

let calendarSpecfications;

let calendarContainer = document.querySelector("#calendarContainer");
// let calendarDates = document.querySelector(".calendar-dates");
// let calendarWeekdays = document.querySelector(".calendar-weekdays");

/*const WEEKDAYS = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
];*/
const WEEKDAYS = ["D", "S", "T", "Q", "Q", "S", "S"];

WEEKDAYS.forEach(function (week) {
    let weekDay = document.createElement("div");
    weekDay.classList.add("weekday");
    weekDay.innerText = week;
    calendarContainer.appendChild(weekDay);
});

let dateElement = document.querySelector(".calendar-date");
const DATE_EL = dateElement.cloneNode(true);
dateElement.remove();
range(1, 31).forEach((v, i) => {
    let el = DATE_EL.cloneNode(true);

    console.log(v);
    el.textContent = v;
    calendarContainer.appendChild(el);
    // dateElement.after(el);
});
// Dias no calendaário
