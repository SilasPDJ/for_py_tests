let getTitle = (retWith) => {

    let doct = document.title
    let returned = doct.split('-')[1].trimStart()
    return [returned.startsWith(retWith), returned]
}
// const toWait = (fun, time) => {
function toWait(fun, time) {
    setTimeout(fun, time, arguments)
}
// arrow functions don't have arguments array



//document.querySelector("#js_CityPosition9SpeedupButton").click()
//document.querySelector("#js_buildingSpeedupActivateBtn").click()


let tempoConstr = document.querySelectorAll("[title='Encurtar tempo de construção']")

while (true) {
    if (getTitle(4)[0]) {

        tempoConstr.forEach(function (e, k, tp) {

            if (e.classList.contains('buildingSpeedupButton')) {
                e.click()
                lastEl = document.querySelector("#js_buildingSpeedupActivateBtn")
                setTimeout(lastEl.click(), 2000)

            }
        })
        break
    }
}