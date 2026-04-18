using System;
using MySql.Data.MySqlClient;

class Program
{
    static string connStr = "server=localhost;user=root;password=;database=QLBH";

    static void Main()
    {
        while (true)
        {
            Console.WriteLine("\n===== MENU =====");
            Console.WriteLine("1. San pham");
            Console.WriteLine("2. Khach hang");
            Console.WriteLine("0. Thoat");

            int c = NhapSo();

            if (c == 1) MenuProduct();
            else if (c == 2) MenuCustomer();
            else break;
        }
    }

    // ===== INPUT SAFE =====
    static int NhapSo()
    {
        int x;
        while (!int.TryParse(Console.ReadLine(), out x))
        {
            Console.Write("Nhap lai: ");
        }
        return x;
    }

    // ================= PRODUCT =================
    static void MenuProduct()
    {
        Console.WriteLine("\n1.Them 2.Hien thi 3.Xoa 4.Tim");
        int c = NhapSo();

        if (c == 1) ThemSP();
        else if (c == 2) HienThiSP();
        else if (c == 3) XoaSP();
        else if (c == 4) TimSP();
    }

    static void ThemSP()
    {
        Console.Write("ID: "); string id = Console.ReadLine();
        Console.Write("Ten: "); string name = Console.ReadLine();
        Console.Write("Nguon goc: "); string origin = Console.ReadLine();
        Console.Write("Gia: "); double price = double.Parse(Console.ReadLine());

        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "INSERT INTO Product VALUES (@id,@name,@origin,@price)";
        var cmd = new MySqlCommand(sql, conn);

        cmd.Parameters.AddWithValue("@id", id);
        cmd.Parameters.AddWithValue("@name", name);
        cmd.Parameters.AddWithValue("@origin", origin);
        cmd.Parameters.AddWithValue("@price", price);

        cmd.ExecuteNonQuery();
        Console.WriteLine("Them thanh cong!");
    }

    static void HienThiSP()
    {
        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "SELECT * FROM Product";
        var cmd = new MySqlCommand(sql, conn);
        var reader = cmd.ExecuteReader();

        while (reader.Read())
        {
            Console.WriteLine($"{reader["Id"]} - {reader["Name"]} - {reader["Origin"]} - {reader["Price"]}");
        }
    }

    static void XoaSP()
    {
        Console.Write("Nhap ID: ");
        string id = Console.ReadLine();

        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "DELETE FROM Product WHERE Id=@id";
        var cmd = new MySqlCommand(sql, conn);
        cmd.Parameters.AddWithValue("@id", id);

        cmd.ExecuteNonQuery();
        Console.WriteLine("Da xoa!");
    }

    static void TimSP()
    {
        Console.Write("Nhap tu khoa: ");
        string k = Console.ReadLine();

        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "SELECT * FROM Product WHERE Id LIKE @k OR Name LIKE @k OR Origin LIKE @k";
        var cmd = new MySqlCommand(sql, conn);
        cmd.Parameters.AddWithValue("@k", "%" + k + "%");

        var reader = cmd.ExecuteReader();

        while (reader.Read())
        {
            Console.WriteLine($"{reader["Name"]}");
        }
    }

    // ================= CUSTOMER =================
    static void MenuCustomer()
    {
        Console.WriteLine("\n1.Them 2.Hien thi 3.Xoa 4.Tim");
        int c = NhapSo();

        if (c == 1) ThemKH();
        else if (c == 2) HienThiKH();
        else if (c == 3) XoaKH();
        else if (c == 4) TimKH();
    }

    static void ThemKH()
    {
        Console.Write("ID: "); string id = Console.ReadLine();
        Console.Write("Ten: "); string name = Console.ReadLine();
        Console.Write("Dia chi: "); string addr = Console.ReadLine();
        Console.Write("SDT: "); string phone = Console.ReadLine();

        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "INSERT INTO Customer VALUES (@id,@name,@addr,@phone)";
        var cmd = new MySqlCommand(sql, conn);

        cmd.Parameters.AddWithValue("@id", id);
        cmd.Parameters.AddWithValue("@name", name);
        cmd.Parameters.AddWithValue("@addr", addr);
        cmd.Parameters.AddWithValue("@phone", phone);

        cmd.ExecuteNonQuery();
        Console.WriteLine("Them thanh cong!");
    }

    static void HienThiKH()
    {
        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "SELECT * FROM Customer";
        var cmd = new MySqlCommand(sql, conn);
        var reader = cmd.ExecuteReader();

        while (reader.Read())
        {
            Console.WriteLine($"{reader["Id"]} - {reader["Name"]} - {reader["Phone"]}");
        }
    }

    static void XoaKH()
    {
        Console.Write("Nhap ID: ");
        string id = Console.ReadLine();

        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "DELETE FROM Customer WHERE Id=@id";
        var cmd = new MySqlCommand(sql, conn);
        cmd.Parameters.AddWithValue("@id", id);

        cmd.ExecuteNonQuery();
        Console.WriteLine("Da xoa!");
    }

    static void TimKH()
    {
        Console.Write("Nhap tu khoa: ");
        string k = Console.ReadLine();

        using var conn = new MySqlConnection(connStr);
        conn.Open();

        string sql = "SELECT * FROM Customer WHERE Id LIKE @k OR Name LIKE @k OR Address LIKE @k OR Phone LIKE @k";
        var cmd = new MySqlCommand(sql, conn);
        cmd.Parameters.AddWithValue("@k", "%" + k + "%");

        var reader = cmd.ExecuteReader();

        while (reader.Read())
        {
            Console.WriteLine($"{reader["Name"]}");
        }
    }
}