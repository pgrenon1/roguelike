var index, components, entities, entitiesID
// var json = require('../data/component_index.json')
$.getJSON("./../data/component_index.json", function (json) {
    index = json
    components = Object.keys(index)
    $("#add-component").click(function () {
        addComponentField(null)
    })
    $("#save-entity").click(saveEntity)
});

$.getJSON("data/entities.json", function (json) {
    entities = json
    entitiesID = Object.keys(entities)
    fillEntitiesSelect($('#entities'))
});


function selectEntity(select) {
    comps = entities[select.options[select.selectedIndex].value]
    $("#id").val(select.options[select.selectedIndex].value)
    $("#content").empty()
    for (var key in comps) {
        addComponentField(key)
        fillSubfieldsValue(comps[key])
    }
}

function fillSubfieldsValue(subs) {
    // console.log(subs)
    for (var sub in subs) {
        value = subs[sub]
        type = index[component][sub]
        // console.log(sub)
        input = $("#" + sub)
        switch (type) {
            case "int":
                // number
                input[0].value = value
                break
            case "str":
                // text
                input[0].value = value
                break
            case "bool":
                // checkbox
                input[0].checked = value
                break
            case "col":
                // color
                r = value[0]
                g = value[1]
                b = value[2]
                value = rgbToHex(r, g, b)

                input[0].value = value
                break
            default:
                // select
                selectedIndex = type.indexOf(value)
                input[0].selectedIndex = selectedIndex
        }
    }
}


function fillEntitiesSelect(select) {
    for (let i = 0; i < entitiesID.length; i++) {
        select.append($("<option />").val(entitiesID[i]).text(entitiesID[i]));
    }
}

function addComponentField(preselected) {
    var newField = $('<div class="component"><label for="type">Type: </label ><select class="componentSelect" onclick="updateOptions(this)" onchange="updateField(this)" name="component-type"></select><button onclick="deleteField(this)">Delete</button><div class="subfields"></div></div>').appendTo("#content")
    fillSelect(newField)
    if (preselected) {
        preSelect(newField, preselected)
    }
}

function preSelect(field, preselected) {
    select = field.find("select")
    select.val(preselected).change()
}

function updateOptions(select) {
    otherSelects = $('.componentSelect')
    opt = select.options
    for (let i = 0; i < otherSelects.length; i++) {
        for (let j = 0; j < opt.length; j++) {
            if (j == otherSelects[i].selectedIndex) {
                opt[j].disabled = true
            }
        }
    }
}

function deleteField(button) {
    button.parentElement.remove();
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

function saveEntity() {
    entity = {}
    comps = $('.component')
    id = $('#id').val()
    for (let i = 0; i < comps.length; i++) {
        componentContent = {}
        // convert comps[i] to jquery object just to use find()
        sel = $(comps[i]).find('select')
        subfields = $(comps[i]).find('.subfields')
        component = sel[0].options[sel[0].selectedIndex].value

        inputs = subfields.children()
        for (let j = 0; j < inputs.length; j++) {
            input = inputs[j].lastChild
            inputLabel = inputs[j].lastChild.id
            type = index[component][inputLabel]
            switch (type) {
                case "int":
                    // number
                    inputValue = parseInt(input.value, 10)
                    break
                case "str":
                    // text
                    inputValue = input.value
                    break
                case "bool":
                    // checkbox
                    inputValue = input.checked
                    break
                case "col":
                    // color
                    var hexValue = input.value.match(/[A-Za-z0-9]{2}/g);
                    var rgbValue = hexValue.map(function (v) { return parseInt(v, 16) });

                    inputValue = rgbValue
                    break
                default:
                    // select
                    inputValue = input.options[input.selectedIndex].value
            }
            componentContent[inputLabel] = inputValue
        }
        entity[component] = componentContent
    }
    entities[id] = entity

    writeToJSON()
}

function writeToJSON() {
    json = JSON.stringify(entities)
    $.post("../server.js", function (data, status) {
        alert("Data: " + data + "\nStatus: " + status);
    });
}

function deleteEntity() {

}

function componentToHex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}