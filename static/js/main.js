$('#btnanswer').on('click', function(){
    console.log('click')
    if($(this).html() == 'Show Answer'){
        $(this).html('Hide Answer')
        // $('.ans').css('visibility','visible')
        $('.ans').animate({opacity:1},'slow')
    } else {
        $(this).html('Show Answer')
        // $('.ans').css('visibility','hidden')
        $('.ans').animate({opacity:0},'slow')
    }
})