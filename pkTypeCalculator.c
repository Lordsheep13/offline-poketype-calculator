#include <stdio.h>
#include <gtk/gtk.h>

static void activate(GtkApplication *app, gpointer user_data){
	GtkWidget *window;
	GtkWidget *stack_switcher;
	GtkWidget *side_stack_atk;
	GtkWidget *side_stack_def;
	GtkWidget *atkbtn;
	GtkWidget *defbtn;

	window = gtk_application_window_new(app);
	gtk_window_set_title(GTK_WINDOW(window),"Window");
	gtk_window_set_default_size(GTK_WINDOW(window),200,200);
	

	stack_switcher = gtk_stack_switcher_new();
	gtk_container_add(GTK_CONTAINER(window),stack_switcher);
	side_stack_atk = gtk_stack_new();
	side_stack_def = gtk_stack_new();

	gtk_stack_switcher_set_stack(GTK_STACK_SWITCHER(stack_switcher),GTK_STACK(side_stack_atk));
	gtk_stack_switcher_set_stack(GTK_STACK_SWITCHER(stack_switcher),GTK_STACK(side_stack_def));

	atkbtn = gtk_button_new_with_label("atk");
	defbtn = gtk_button_new_with_label("def");
	gtk_stack_add_titled(GTK_STACK(side_stack_atk),atkbtn,"button","page2");
	gtk_stack_add_titled(GTK_STACK(side_stack_def),defbtn,"button","page1");

	gtk_widget_show_all(window);
}

int main(int argc,char **argv){

	GtkApplication *app;
	int status;

	app = gtk_application_new("pokemon.type.calculator",G_APPLICATION_DEFAULT_FLAGS);
	g_signal_connect(app,"activate",G_CALLBACK(activate),NULL);
	status = g_application_run(G_APPLICATION(app),argc,argv);
	g_object_unref(app);

	return status;
}
