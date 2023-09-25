for (double t = 0.0; true; t = t + dt)
 for (int i = 0; i < N; i++)
 {
 bodies[i].resetForce();
 for (int j = 0; j < N; j++)
 if (i != j)
 bodies[i].addForce(bodies[j]);

 // 

 public static void main(String[] args)
{
 int N = StdIn.readInt();
 UF uf = new UF(N);
 while (!StdIn.isEmpty())
 {
 int p = StdIn.readInt();
 int q = StdIn.readInt();
 if (!uf.connected(p, q))
 {
 uf.union(p, q);
 StdOut.println(p + " " + q);