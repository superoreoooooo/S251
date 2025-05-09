namespace p0509;

class Program
{
    public delegate void TestDelegate();

    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        for (int i = 0; i < 10; i++) {
            Thread tr = new Thread(() => {
                Console.WriteLine("ASDF");
                try {
                    Thread.Sleep(1000);
                } catch(Exception e) {
                    
                }
                Console.WriteLine("FDSA");
            });
            tr.Start();
        }
    }
}
