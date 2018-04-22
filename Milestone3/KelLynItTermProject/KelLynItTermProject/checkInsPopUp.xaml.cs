using Npgsql;
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
using System.Windows.Shapes;

namespace KelLynItTermProject
{
    /// <summary>
    /// Interaction logic for checkInsPopUp.xaml
    /// </summary>
    public partial class checkInsPopUp : Window
    {
        /// <summary>
        /// Builder for string to connect to the database.
        /// </summary>
        /// <returns>string to connect to database.</returns>
        private string buildConnString()
        {
            return "Host=localhost; Username=postgres; Password=Anjaroonie7; Database=project;";
        }

        public checkInsPopUp(string selectedBusiness)
        {
            InitializeComponent();
            checkInColumnChart(selectedBusiness);
        }

        private void checkInColumnChart(string selectedBusiness)
        {
            List<KeyValuePair<string, int>> chartData = new List<KeyValuePair<string, int>>();
            using (var comm = new NpgsqlConnection(buildConnString()))
            {

                comm.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = comm;
                    cmd.CommandText = "SELECT day, sum(morning + afternoon + evening + night) FROM checkins WHERE business_id = '" + selectedBusiness + "' GROUP BY day ORDER BY day; ";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            chartData.Add(new KeyValuePair<string, int>(reader.GetString(0), reader.GetInt32(1)));
                        }
                    }
                }
                comm.Close();
            }
            checkinChart.DataContext = chartData;
        }
    }
}
