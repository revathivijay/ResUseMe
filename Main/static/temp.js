$(document).ready(function () {
    $('form').on('submit', function (event) {
        console.log('Entered submit')
        $.ajax({
            data: {
                filter_name: $('#filters').val(),
                job_post_name: $('#job_post').val(),
            },
            type: 'POST',
            url: '/temp'
        })
            .done(function (data) {
                $('#job_post_name').text(data.job_post).show();
                $('#filter_name').text(data.filter).show();
                var node = document.getElementById("skill_id");
                while (node.firstChild) {
                    node.removeChild(node.firstChild);
                }

                for (var i = 0; i < data.skills.length; i++){
                    var btn_id = "btn_" + i;
                    var div_id = "div_" + i;
                    var a1 = "<div class='skill_item_subclass'><p class ='col-sm-8 skill_para' id=";
                    var a2 = "></p><button class = 'col-sm-1 cancel_btn' id=" + "btn_" + i + " onclick='cancel_clicked(this.id)'>x</button></div >";
                    //creating div element
                    var divv = document.createElement("div");
                    divv.className = 'card skill_item_class';
                    divv.id = div_id;
                    divv.innerHTML = a1 + i + a2;
                    //appending div element in a bigger div element
                    document.getElementById("skill_id").appendChild(divv);
                    
                    var text = document.createTextNode(data.skills[i]);
                    var para = document.getElementById(i);
                    console.log("para initialised");
                    para.appendChild(text);
                    console.log("para appended");
                }

                //to add skill
                var a3 = "<div class='skill_item_subclass'><p class ='col-sm-8 skill_para' id=";
                var a4 = ">Add Skills here</p><button class = 'col-sm-1 add_btn' id=" + "btn_" + 12 + " onclick='#'>+</button></div >";
                //creating div element
                var divv_ = document.createElement("div");
                divv_.className = 'card add_skill_button';
                divv_.id = "div_10";
                divv_.innerHTML = a3 + 10 + a4;
                //appending div element in a bigger div element
                document.getElementById("skill_id").appendChild(divv_);

            });
        event.preventDefault();
    });
});



function cancel_clicked(id) {
    console.log(id+"wda");
    
    var id_no = id.substring(id.length - 1, id.length);
    console.log("div_" + id_no);
    
    var to_remove = document.getElementById("div_" + id_no);
    to_remove.parentNode.removeChild(to_remove);
}
