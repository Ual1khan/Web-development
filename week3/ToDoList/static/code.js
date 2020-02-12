var totRows = 0
var table = document.getElementById("list");


function addClicked(){
    var inputValue = document.getElementById("input-text").value;
    var row = table.insertRow(totRows)
    var cell1 = row.insertCell()
    var cell2 = row.insertCell()
    var cell3 = row.insertCell()

    if(inputValue !== ''){
        cell2.innerHTML = inputValue
        cell3.innerHTML = 'X'
        totRows++
        document.getElementById("input-text").value = ""


        var chckbox=document.createElement('input');
            chckbox.type='checkbox';
            cell1.appendChild(chckbox);

        chckbox.onclick = function(){
            if(cell2.className!='done')
                cell2.classList.add("done");
        else cell2.classList.remove("done");

        }
        cell3.onclick = function(){
            var rowdel = cell3.parentNode;
            row.parentNode.removeChild(row);
        }
    
    }
}

