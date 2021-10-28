import range from "./range_function.js";
let mainContainer = document.querySelector(".container");

function getDate(date) {
    return `${d.getDate()}/${d.getMonth()}/${d.getFullYear()}`;
}

const d = new Date(2021, 10, 27);

let calendarContainer = document.querySelector("#calendarContainer");
// let calendarDates = document.querySelector(".calendar-dates");
// let calendarWeekdays = document.querySelector(".calendar-weekdays");

const WEEKDAYS = ["D", "S", "T", "Q", "Q", "S", "S"];

// Dias no calendaário
let dateElement = document.querySelector(".calendar-date");
const DATE_EL = dateElement.cloneNode(true);
dateElement.remove();

function changeCalendar(weekDay, lastDate) {
    calendarContainer.innerHTML = "";
    // cria dias da semana
    WEEKDAYS.forEach(function (week) {
        let weekDay = document.createElement("div");
        weekDay.classList.add("weekday");
        weekDay.innerText = week;
        calendarContainer.appendChild(weekDay);
    });
    // Sinaliza em que dia da semana começa o mês
    for (let i = 0; i < weekDay; i++) {
        calendarContainer.appendChild(document.createElement("div"));
    }

    //
    range(1, lastDate + 1).forEach((v, i) => {
        let el = DATE_EL.cloneNode(true);
        // console.log(v);
        el.textContent = v;
        calendarContainer.appendChild(el);
        // dateElement.after(el);
    });
}

// Selecionar meses select
const selectMonth = document.querySelector("#selectMonth");
const selectYear = document.querySelector("#selectYear");

const MONTHS = Array.from(new Array(12).keys());

let nameMonths = MONTHS.map((name) => {
    let date = new Date(new Date().getFullYear(), name, 1);
    return date.toLocaleString("default", { month: "long" });
});
// range() function

let selectOpts = (array, select) => {
    array.forEach((v, i, ar) => {
        let selectOpt = document.createElement("option");
        let val = i;
        let txt = v;
        // para dar o value numerico aos meses
        selectOpt.value = txt == val + ar[0] ? txt : i + 1;
        selectOpt.text = String(v).toUpperCase();
        select.appendChild(selectOpt);
    });
};

selectOpts(nameMonths, selectMonth);
selectOpts(range(1900, 3000), selectYear);

selectYear.value = new Date().getFullYear();

let criaCalendario = () => {
    let firstDay, lastDay;
    let month = selectMonth.value;
    let year = selectYear.value;
    firstDay = new Date(year, month - 1, 1);
    lastDay = new Date(year, month, 0);
    let lastDayDate = lastDay.getDate();

    // console.log(firstDay.getMonth(), lastDay.getMonth());

    let firstDayweek = firstDay.getDay();
    changeCalendar(firstDayweek, lastDayDate);
};
// TODO: ARRUMAR A QUANTIDADE DOS MESES, ELE TA ENTENDENDO JANEIRO COMO 0
// APESAR DISSO O DIA DAS SEMANAS E O INÍCIO DO DIA 1 TA CERTO

selectMonth.addEventListener("click", criaCalendario);
selectMonth.addEventListener("change", criaCalendario);
selectYear.addEventListener("click", criaCalendario);
selectYear.addEventListener("change", criaCalendario);

document.getElementsByTagName("body").onload = criaCalendario();
