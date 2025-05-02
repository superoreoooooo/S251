using ConsoleApp1;

public class p0418 {
    public static void Main() {
        Point point = new Point(10, 20);

        //Console.WriteLine(point.a + " " + point.b);

        List<Product> list = new List<Product>() {
            new Product() {name = "a", price = 10},
            new Product() {name = "b", price = 20},
            new Product() {name = "c", price = 30}
        };

        list.Sort();

        foreach (var item in list) {
            Console.WriteLine(item);
        }

        Dummy dummy = new Dummy();

        dummy.Dispose();

        TestClass tc = new TestClass();
        Console.WriteLine(tc.TestInstanceMethod());

        Test2 t2 = new Test2();
        TestClass t1 = new Test2();
        IDisposable id = new Test2();
        IComparable ic = new Test2();
    }

    struct Point {
        public int a;
        public int b;

        public Point(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    class Product : IComparable
    {
        public string name {get; set;}
        public int price {get; set;}

        public int CompareTo(object? obj)
        {
            return this.price.CompareTo((obj as Product).price);
        }

        public override string ToString()
        {
            return name + " : " + price + " Won";
        }
    }

    class Dummy : IDisposable
    {
        public void Dispose()
        {
            Console.WriteLine("ASdf");
        }
    }

    class TestClass : IBasic
    {
        public int TestProperty { get => throw new NotImplementedException(); set => throw new NotImplementedException(); }

        public int TestInstanceMethod()
        {
            Console.WriteLine("hello");
            return 0;
        }
    }

    class Test2 : TestClass, IDisposable, IComparable
    {
        public int CompareTo(object? obj)
        {
            throw new NotImplementedException();
        }

        public void Dispose()
        {
            throw new NotImplementedException();
        }
    }
}