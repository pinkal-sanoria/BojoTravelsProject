
// navbar silder
const body=document.body;
let lastscroll=0
window.addEventListener('scroll',()=>{
    const currentscroll = window.pageYOffset
    if(currentscroll<=0){
        body.classList.remove('scroll-up')
    }
    if(currentscroll>lastscroll && !body.classList.contains("scroll-down")){
        body.classList.remove('scroll-up')
        body.classList.add('scroll-down')
    }
    if(currentscroll<lastscroll && body.classList.contains("scroll-down")){
        body.classList.remove('scroll-down')
        body.classList.add('scroll-up')
    }
    lastscroll=currentscroll
})



// ====================== dropdown menu toggle function ==================

const toggleBtn= document.querySelector('.toggle-btn')
const toggleBtnIcon= document.querySelector(".toggle-btn i")
const dropDownMenu = document.querySelector('.dropdown_menu')

toggleBtn.onclick=function(){
    dropDownMenu.classList.toggle('open')
    const isOpen= dropDownMenu.classList.contains('open')

    toggleBtnIcon.classList= isOpen 
    ? 'bi bi-x-square-fill'
    : 'bi bi-slack'
}



// ======================== calender ====================

$(document).ready(function() {

            
    let dt = new Date();
    let month = dt.getMonth()+1 //as it will return value between 0-11 so to make it 1-12 we add 1 to it
    let year = dt.getFullYear();
    let currentDay = dt.getDate();
    var defaultDateSet=currentDay+"-"+month +'-'+year
    ////////
    $(function() {
        $("#my_date_picker1").datepicker({
            minDate:0,
            dateFormat: "yy-mm-dd",
            yearRange: "-100:+20",
            beforeShowDay: my_check


        });
    });

    function my_check(in_date) {
        in_date = in_date.getDate() + '/'
        + (in_date.getMonth() + 1) + '/' + in_date.getFullYear();
        
        var my_array = new Array('11/3/2023', '18/3/2023','8/3/2023','25/3/2023');
        //$('#d1').append(in_date+'<br>')
        if (my_array.indexOf(in_date) >= 0) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }
})
