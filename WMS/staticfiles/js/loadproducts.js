const user_input=$("#user-input")
const search_icon = $("#search_icon")
const produse_div = $("#replaceable-content")
const endpoint = ""
const delay_by_in_ms = 700
let schedule_function = false

let ajax_call = function(endpoint,request_parameters){
    $.getJSON(endpoint,request_parameters).done(response =>{
        produse_div.fadeTo("slow",0).promise().then(()=>{
            produse_div.html(response['html_from_view'])
            produse_div.fadeTo("slow",1)
            search_icon.removeClass('blink')
        })
    })
}
user_input.on('keyup',function(){
    const request_parameters = {
        q: $(this).val() }
        search_icon.addClass('blink')
    if (schedule_function) {
        clearTimeout(schedule_function)
    }
    schedule_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
    
})