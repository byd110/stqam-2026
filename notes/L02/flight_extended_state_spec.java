// Meszaros, p. 471
// extended state specification
public void testRemoveFlightLogging_NSC() {
 // arrange:
 FlightDto expectedFlightDto=createRegisteredFlight();
 FlightMgmtFacade=new FlightMgmtFacadeImpl();
 // act:
 facade.removeFlight(expectedFlightDto.getFlightNo());
 // assert:
 assertFalse("flight still exists after removed",
             facade.flightExists(expectedFlightDto,
				 getFlightNo()));
}
