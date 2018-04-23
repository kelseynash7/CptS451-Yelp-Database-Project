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
    /// Interaction logic for ReviewsPopUp.xaml
    /// </summary>
    public partial class ReviewsPopUp : Window
    {
        public ReviewsPopUp(string selectedBusiness)
        {
            InitializeComponent();
            ReviewsChart(selectedBusiness);
        }

        private void ReviewsChart(string selectedBusiness)
        {
            //List<List<string>> reviewData = new List<List<string>>();
            List<Review> reviewData = new List<Review>();
            using (var comm = new NpgsqlConnection("Host=localhost; Username=postgres; Password=Anjaroonie7; Database=project"))
            {
                comm.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = comm;
                    cmd.CommandText = "SELECT date, users.name, review.stars, review.text, review.funny, review.useful, review.cool FROM business, review, users WHERE business.business_id = review.business_id AND users.user_id = review.user_id AND review.business_id = '" + selectedBusiness + "' ORDER BY review.date desc;";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            //reviewData.Add(new List<string> { reader.GetDateTime(0).ToString(), reader.GetString(1), reader.GetDouble(2).ToString(), reader.GetString(3), reader.GetInt32(4).ToString(), reader.GetInt32(5).ToString(), reader.GetInt32(6).ToString()});
                            reviewData.Add(new Review() { Date = reader.GetDate(0).ToString(), UserName = reader.GetString(1), Stars = reader.GetDouble(2).ToString(), Text = reader.GetString(3), Funny = reader.GetInt32(4).ToString(), Useful = reader.GetInt32(5).ToString(), Cool = reader.GetInt32(6).ToString() });
                        }
                    }
                }
                comm.Close();
            }
            ReviewsView.ItemsSource = reviewData;
        }
    }

    public class Review
    {
        public string Date { get; set; }
        public string UserName { get; set; }
        public string Stars { get; set; }
        public string Text { get; set; }
        public string Funny { get; set; }
        public string Useful { get; set; }
        public string Cool { get; set; }
    }
}
