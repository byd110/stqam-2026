[Test]
public void GetMinimum_UnsortedIntegerArray_ReturnsSmallestValue() 
{   
  var unsortedArray = new int[] {7,4,9,2,5}; // Arrange     
  var minimum = Statistics.GetMinimum(unsortedArray); // Act     
  Assert.AreEqual(2, minimum); // Assert 
}
