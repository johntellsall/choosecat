describe('My First Test', function() {
  it('Does not do much!', function() {
    expect(true).to.equal(true)
  })
})
describe('The Home Page', function() {
  it('says Hello', function() {
    cy.visit('/')
    console.log(cy.get('body').contains('Hello'))
  })
})
