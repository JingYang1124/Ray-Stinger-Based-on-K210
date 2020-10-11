
def Blob_Handler (Blobs,Old_X,Old_Y):
  Sum_X = 0
  Sum_Y = 0
  n = 0
  Min_X = 160
  Max_X = 160
  Min_Y = 120
  Max_Y = 120
  for b in Blobs:
    X = b[5]
    Y = b[6]
    #if Y > 110:
    Sum_X = Sum_X + X
    Sum_Y = Sum_Y + Y
    if n == 0:
      Min_X = X
      Max_X = X
      Min_Y = Y
      Max_Y = Y
    else:
      if X < Min_X:
        Min_X = X
      if X > Max_X:
        Max_X = X
      if Y < Min_Y:
        Min_Y = Y
      if Y > Max_Y:
        Max_Y = Y
    n += 1
  Dis_Max_2 = (Max_Y - Min_Y)^2 + (Max_X - Min_X)^2
  if n >= 1 and Sum_X > 0 and Sum_Y > 0:
    Ave_X = Sum_X / n
    Ave_Y = Sum_Y / n
  else:
    Ave_X = Old_X
    Ave_Y = Old_Y
  #New_X = 0.6 * Old_X + 0.4 * Ave_X
  #New_Y = 0.6 * Old_Y + 0.4 * Ave_Y
  New_X = 0 * Old_X + 1 * Ave_X
  New_Y = 0 * Old_Y + 1 * Ave_Y
  return New_X, New_Y, Dis_Max_2
