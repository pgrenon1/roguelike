from tkinter import *
import pyclbr
import inspect
import components
import json


class ComponentField:
    def __init__(self, master, comp_to_annotations, x, y):
        self.master = master
        self.group = LabelFrame(master, text="", padx=5, pady=5)
        self.group.grid(padx=10, pady=10, row=x, column=y, sticky=N+W)
        self.comp_to_annotations = comp_to_annotations
        self.select = self.instantiate_select()
        self.component_holding_var
        # to hold a label/entry pair
        self.subframes = []
        self.tk_dict = {}
        self.delete_component_button = self.create_delete_button()
        self.render_order_holding_var = StringVar(self.group)
        # self.comp_data = {}

    def create_delete_button(self):
        delete_button = Button(self.group, text="Delete Component")
        delete_button.grid(sticky=N+W)
        delete_button["command"] = self.delete_component_field

    def delete_component_field(self):
        app.remove_component_field(self)

    def instantiate_select(self):
        self.component_holding_var = StringVar(self.master)
        self.component_holding_var.set("Choose a Component Type")
        newSelect = OptionMenu(self.group, self.component_holding_var,
                               *self.comp_to_annotations)
        self.component_holding_var.trace('w', self.update_component_fields)
        newSelect.grid()

    def update_component_fields(self, *args):
        for field_pair in self.subframes:
            # forget every label and input
            for child in field_pair.winfo_children():
                child.grid_forget()
            # forget every field that held a label and input pair
            field_pair.grid_forget()

        for comp in self.comp_to_annotations:
            if comp == self.component_holding_var.get():
                # set a label to the ComponentField
                self.group["text"] = comp
                # for each needed args
                for arg_name in self.comp_to_annotations[comp]:
                    arg_type = self.comp_to_annotations[comp][arg_name]
                    # make a group label+input
                    new_field = Frame(self.group, padx=5, pady=5)
                    self.subframes.append(new_field)
                    new_field.grid()
                    # add label
                    label = Label(new_field, text=arg_name)
                    label.grid(sticky=W)
                    # add input
                    if arg_name == "render_order":
                        # self.render_order_holding_var = StringVar(new_field)
                        self.render_order_holding_var.set(
                            "Choose a RenderOrder")
                        render_order_select = OptionMenu(
                            new_field, self.render_order_holding_var, *app.render_order_options)

                        render_order_select.grid(sticky=E)
                        self.tk_dict[label] = self.render_order_holding_var.get()
                    else:
                        if arg_type is int:
                            vcmd = (self.group.register(self.validate),
                                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
                            entry = Entry(
                                new_field, validate='key', validatecommand=vcmd)
                        else:
                            entry = Entry(new_field)
                        self.tk_dict[label] = entry
                    entry.grid(sticky=E)

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if action == '1':
            if text in '0123456789.-':
                try:
                    int(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.id_var = StringVar(self)
        self.frame = self.create_component_frame()
        self.render_order_options = None
        self.id_group = None
        self.id_entry = self.create_id_entry()
        self.save_button = self.create_save_button()
        self.new_button = self.create_clear_button()
        self.comp_to_annotations = self.get_comp_to_annotations()
        self.create_add_button()
        self.component_fields = []
        self.data = {}
        self.get_file_data()
        self.list_box = self.create_list_box()
        self.update_list_box()

    def create_list_box(self):
        list_box_frame = Frame(self, bd=2)
        list_box_frame.grid_rowconfigure(0, weight=1)
        list_box_frame.grid_columnconfigure(0, weight=1)
        list_box_frame.grid(row=6, column=0)

        scrollbar = Scrollbar(list_box_frame)
        scrollbar.grid(row=6, column=1, sticky=N+S)

        list_box = Listbox(
            list_box_frame, yscrollcommand=scrollbar.set)
        list_box.grid(row=6, column=0, sticky=N+S+E+W)
        list_box.bind("<<ListboxSelect>>", self.show_comps_for_selected)

        scrollbar.config(command=list_box.yview)

        return list_box

    def show_comps_for_selected(self, event):
        # Make sure only one entity is selected
        if len(self.list_box.curselection()) > 1:
            for i in self.list_box.curselection():
                if i not in self.selection:
                    self.list_box.selection_clear(i)
        self.selection = self.list_box.curselection()

        self.clear_all()

        # create and fill ComponentFields
        selected_entity = self.list_box.get(ACTIVE)
        self.id_entry.delete(0, END)
        self.id_entry.insert(0, selected_entity)

        for comp in self.data[selected_entity]:
            new_comp_field = self.add_component_field()
            new_comp_field.component_holding_var.set(comp)
            for subframe in new_comp_field.subframes:
                arg_name = subframe.winfo_children()[0]["text"]
                if arg_name == "render_order":
                    new_comp_field.render_order_holding_var.set(
                        app.data[selected_entity][comp][arg_name])
                else:
                    entry = subframe.winfo_children()[1]
                    entry.insert(0, app.data[selected_entity][comp][arg_name])

    def update_list_box(self):
        for entry in self.data:
            if not entry in self.list_box.get(0, END):
                self.list_box.insert(END, entry)

    def get_file_data(self):
        with open('data/entities2.json', 'r') as infile:
            self.data = json.load(infile)

    def create_component_frame(self):
        frame = LabelFrame(self, text="Components")
        frame.grid(row=0, column=2, columnspan=20, rowspan=20,
                   sticky=W+E+N+S)
        frame.grid_columnconfigure(0, minsize=600)

        canvas = Canvas(frame, bg="gray", width=300,
                        height=300, scrollregion=(0, 0, 500, 1000))
        canvas.grid(sticky=W+E+N+S)

        scrollbar = Scrollbar(frame)
        scrollbar.grid(row=0, sticky=E+N+S)
        scrollbar.config(command=canvas.yview)

        canvas.config(yscrollcommand=scrollbar.set)

        return canvas

    def create_save_button(self):
        save_button = Button(
            self, text="Save Entity")
        save_button["command"] = self.save
        save_button.grid(sticky=W, row=3, column=0)
        return save_button

    def create_clear_button(self):
        new_clear_button = Button(self, text="Clear")
        new_clear_button["command"] = self.clear_all
        new_clear_button.grid(sticky=W, row=4, column=0)
        return new_clear_button

    def clear_all(self):
        for child in self.frame.winfo_children():
            if child is self.id_group:
                self.id_entry.delete(0, END)
            else:
                child.destroy()
        self.component_fields = []

    def create_id_entry(self):
        frame = Frame(self.frame)
        frame.grid(row=0, column=0, sticky=W)
        self.id_group = frame

        id_label = Label(frame, text="Entity ID")
        id_label.grid(sticky=W, row=0, column=0)

        id_entry = Entry(frame)
        id_entry.grid(sticky=W, row=0, column=1)
        return id_entry

    def create_add_button(self):
        self.b = Button(self, text="Add Component")
        self.b.grid(sticky=W+N, row=2, column=0)
        self.b["command"] = self.add_component_field

    def add_component_field(self):
        new_component = ComponentField(
            self.frame, self.comp_to_annotations, int(len(self.component_fields) / 8)+1, int(len(self.component_fields) % 8))
        self.component_fields.append(new_component)

        return new_component

    def remove_component_field(self, to_remove):
        to_remove.group.grid_forget()
        self.component_fields.remove(to_remove)

    def get_comp_to_annotations(self):
        module_name = "components"
        module = pyclbr.readmodule(module_name)
        del module["Enum"]
        # del module["RenderOrder"]
        class_to_annotations = {}
        for class_object in module:
            clazz = getattr(sys.modules[module_name], class_object)
            if type(clazz) is enum.EnumMeta:
                self.render_order_options = [e.name for e in clazz]
                print(self.render_order_options)
            else:
                class_name = class_object
                signature = inspect.getfullargspec(clazz)

                if not signature.annotations:
                    class_to_annotations[class_object] = {}
                else:
                    class_to_annotations[class_object] = signature.annotations

        return class_to_annotations

    def save(self):
        with open('data/entities.json') as json_file:
            self.data = json.load(json_file)

        # create json object
        new_entity_data = {}
        for cf in self.component_fields:
            comp_data = {}
            comp_name = cf.component_holding_var.get()
            if cf.tk_dict:
                for member in cf.tk_dict:
                    label = member["text"]
                    arg_type = self.comp_to_annotations[comp_name][label]
                    print(arg_type)
                    if arg_type is int:
                        input_data = cf.tk_dict[member].get()
                        comp_data[label] = int(input_data)
                    else:
                        input_data = cf.tk_dict[member].get()
                        comp_data[label] = input_data
                if comp_data:
                    self.data[comp_name] = comp_data
            else:
                self.data[comp_name] = {}

        # self.data[self.id_var.get()] = new_entity_data

        # self.write_to_file()
        # self.update_list_box()

    def write_to_file(self):
        with open('data/entities2.json', 'w') as outfile:
            json.dump(data, outfile)


root = Tk()
root.title("Entity Creator")
root.geometry("900x500")
app = Application(root)
root.mainloop()
