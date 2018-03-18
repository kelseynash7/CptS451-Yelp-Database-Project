using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace KelLynItTermProject
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            addColumns2Grid();
        }

        public void addColumns2Grid()
        {
            DataGridTextColumn column = new DataGridTextColumn();
            column.Header = "BusinessName";
            column.Binding = new Binding("name");
            resultsGrid.Columns.Add(column);

            DataGridTextColumn column1 = new DataGridTextColumn();
            column1.Header = "Address";
            column1.Binding = new Binding("address");
            resultsGrid.Columns.Add(column1);

            DataGridTextColumn column2 = new DataGridTextColumn();
            column2.Header = "City";
            column2.Binding = new Binding("city");
            resultsGrid.Columns.Add(column2);

            DataGridTextColumn column3 = new DataGridTextColumn();
            column3.Header = "State";
            column3.Binding = new Binding("state");
            resultsGrid.Columns.Add(column3);

            DataGridTextColumn column4 = new DataGridTextColumn();
            column4.Header = "Distance (miles)";
            column4.Binding = new Binding("distance");
            resultsGrid.Columns.Add(column4);

            DataGridTextColumn column5 = new DataGridTextColumn();
            column5.Header = "Stars";
            column5.Binding = new Binding("stars");
            resultsGrid.Columns.Add(column5);

            DataGridTextColumn column6 = new DataGridTextColumn();
            column6.Header = "# of Reviews";
            column6.Binding = new Binding("reviews");
            resultsGrid.Columns.Add(column6);

            DataGridTextColumn column7 = new DataGridTextColumn();
            column7.Header = "Avg Review Rating";
            column7.Binding = new Binding("avgRating");
            resultsGrid.Columns.Add(column7);

            DataGridTextColumn column8 = new DataGridTextColumn();
            column8.Header = "Total CheckIns";
            column8.Binding = new Binding("checkIns");
            resultsGrid.Columns.Add(column8);
        }
    }
}
