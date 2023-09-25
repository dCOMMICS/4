for (double t = 0.0; true; t = t + dt)
 for (int i = 0; i < N; i++)
 {
 bodies[i].resetForce();
 for (int j = 0; j < N; j++)
 if (i != j)
 bodies[i].addForce(bodies[j]);

 // 