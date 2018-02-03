using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using Npgsql;

namespace Milestone1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        /// <summary>
        /// The Business class.
        /// </summary>
        public class Business
        {
            public string name { get; set; }
            public string state { get; set; }
            public string city { get; set; }
        }

        /// <summary>
        /// Builder for string to connect to the database.
        /// </summary>
        /// <returns>string to connect to database.</returns>
        private string buildConnString()
        {
            return "Host=localhost; Username=postgres; Password=Abigail1; Database=business;";
        }

        /// <summary>
        /// Initialize the main window.
        /// </summary>
        public MainWindow()
        {
            InitializeComponent();
            AddStates();
            AddCities();
            addColumns2Grid();
        }

        /// <summary>
        /// Add the states from the database.
        /// </summary>
        public void AddStates()
        {
            using (var comm = new NpgsqlConnection(buildConnString()))
            {
                comm.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = comm;
                    cmd.CommandText = "SELECT DISTINCT state FROM business ORDER BY state;";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            stateList.Items.Add(reader.GetString(0));
                        }
                    }
                }
                comm.Close();
            }
        }

        /// <summary>
        /// Add the cities from the database.
        /// </summary>
        public void AddCities()
        {
            using (var comm = new NpgsqlConnection(buildConnString()))
            {
                comm.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = comm;
                    cmd.CommandText = "SELECT DISTINCT city FROM business ORDER BY city;";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            cityList.Items.Add(reader.GetString(0));
                        }
                    }
                }
                comm.Close();
            }
        }

        /// <summary>
        /// Add the cities from the database for the selected state.
        /// </summary>
        public void AddCitiesWhenStateSelected()
        {
            using (var comm = new NpgsqlConnection(buildConnString()))
            {
                cityList.Items.Clear();
                comm.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = comm;
                    cmd.CommandText = "SELECT DISTINCT city FROM business WHERE state = '"+ stateList.SelectedItem.ToString()+"'ORDER BY city;";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            cityList.Items.Add(reader.GetString(0));
                        }
                    }
                }
                comm.Close();
            }
        }

        /// <summary>
        /// Add the columns to the grid.
        /// </summary>
        public void addColumns2Grid()
        {
            DataGridTextColumn column = new DataGridTextColumn();
            column.Header = "Business Name";
            column.Width = 255;
            column.Binding = new Binding("name");
            businessGrid.Columns.Add(column);

            DataGridTextColumn column2 = new DataGridTextColumn();
            column2.Header = "State";
            column2.Binding = new Binding("state");
            businessGrid.Columns.Add(column2);

            DataGridTextColumn column3 = new DataGridTextColumn();
            column3.Header = "City";
            column3.Binding = new Binding("city");
            businessGrid.Columns.Add(column3);
        }

        /// <summary>
        /// Add the businesses to the datagrid based on selected state.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void stateList_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            businessGrid.Items.Clear();
            if (stateList.SelectedIndex > -1)
            {
                using (var comm = new NpgsqlConnection(buildConnString()))
                {
                    comm.Open();
                    using (var cmd = new NpgsqlCommand())
                    {
                        cmd.Connection = comm;
                        cmd.CommandText = "SELECT name,state,city FROM business WHERE state='" + stateList.SelectedItem.ToString() + "';";
                        using (var reader = cmd.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                businessGrid.Items.Add(new Business() { name = reader.GetString(0), state = reader.GetString(1), city = reader.GetString(2) });
                            }
                        }
                    }
                    comm.Close();
                }
                AddCitiesWhenStateSelected();
            }
        }

        /// <summary>
        /// Add the businesses to the datagrid based on selected city
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void cityList_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            businessGrid.Items.Clear();

            if (cityList.SelectedIndex > -1)
            {
                using (var comm = new NpgsqlConnection(buildConnString()))
                {
                    comm.Open();
                    using (var cmd = new NpgsqlCommand())
                    {
                        cmd.Connection = comm;
                        cmd.CommandText = "SELECT name,state, city FROM business WHERE city='" + cityList.SelectedItem.ToString() + "' ORDER BY name;";
                        using (var reader = cmd.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                businessGrid.Items.Add(new Business() { name = reader.GetString(0), state = reader.GetString(1), city = reader.GetString(2) });
                            }
                        }
                    }
                    comm.Close();
                }
            }
        }
    }
}
