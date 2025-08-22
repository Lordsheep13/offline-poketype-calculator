#include <stdio.h>
#include <gtk/gtk.h>

static void activate(GtkApplication *app, gpointer user_data){
	GtkWidget *window;
	GtkWidget *grid;
	GtkWidget *calcbtn;

	window = gtk_application_window_new(app);
	gtk_window_set_title(GTK_WINDOW(window),"Window");
	gtk_window_set_default_size(GTK_WINDOW(window),200,200);
	
	grid = gtk_grid_new();
	gtk_container_add(GTK_CONTAINER(window),grid);

	calcbtn = gtk_button_new_with_label("calculate");
	gtk_grid_attach(GTK_GRID(grid),calcbtn,0,0,2,1);

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
