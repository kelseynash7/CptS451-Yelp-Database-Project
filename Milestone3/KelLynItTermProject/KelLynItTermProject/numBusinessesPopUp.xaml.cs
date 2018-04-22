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
    /// Interaction logic for numBusinessesPopUp.xaml
    /// </summary>
    public partial class numBusinessesPopUp : Window
    {
        public numBusinessesPopUp(string selectedCity)
        {
            InitializeComponent();
            numBusinessesChart(selectedCity);
        }

        private void numBusinessesChart(string selectedCity)
        {
            List<KeyValuePair<string, int>> businessChartData = new List<KeyValuePair<string, int>>();
            using (var conn = new NpgsqlConnection("Host=localhost; Username=postgres; Password=Anjaroonie7; Database=project"))
            {
                conn.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = conn;

                    // retrieve rows
                    cmd.CommandText = "select postal_code, count(business_id) from business where city= '" + selectedCity + "' group by postal_code order by postal_code; ";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            businessChartData.Add(new KeyValuePair<string, int>(reader.GetString(0), reader.GetInt32(1)));
                        }
                    }
                }
            }

            businessPerZipcode.DataContext = businessChartData;
        }
    }
}
