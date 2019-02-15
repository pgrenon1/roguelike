var index, components
// var json = require('../data/component_index.json')
$.getJSON("../data/component_index.json", function (json) {
    index = json
    components = Object.keys(index)
    $("#add-component").click(addComponentField)
});

function addComponentField() {
    $("body").append
    var newField = $('<div class="component"><label for="type">Type: </label ><select onchange="updateField(this)" name="component-type"></select><div class="subfields"></div></div>').appendTo("#content")
    fillSelect(newField)
}

function fillSelect(field) {
    select = field.find("select")
    for (let i = 0; i < components.length; i++) {
        select.append($("<option />").val(components[i]).text(components[i]));
    }
}

function updateField(select) {
    component = select.options[select.selectedIndex].value
    subfields = index[component]
    keys = Object.keys(subfields)
    newSubfields = $('<div />').attr({ class: "subfields" })
    for (let i = 0; i < keys.length; i++) {
        labelText = keys[i]
        var label = $("<label>").text(labelText + ": ");
        var input
        type = subfields[keys[i]]
        switch (type) {
            case "int":
                // number
                input = $('<input type="number">').attr({ id: labelText, name: labelText });
                break
            case "str":
                // text
                input = $('<input type="text">').attr({ id: labelText, name: labelText });
                break
            case "bool":
                // checkbox
                input = $('<input type="checkbox">').attr({ id: labelText, name: labelText });
                break
            case "col":
                // color
                input = $('<input type="color">').attr({ id: labelText, name: labelText });
                break
            default:
                // select
                input = $('<select>').attr({ id: labelText, name: labelText })
                for (let j = 0; j < type.length; j++) {
                    input.append($("<option />").val(type[j]).text(type[j]));
                }
        }
        input.appendTo(label);
        newSubfields.append(label);
    }
    $(select).parent().find(".subfields").replaceWith(newSubfields);
}