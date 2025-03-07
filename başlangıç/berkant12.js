// "5.5.5.5.5" output => "5[.]5[.]5[.]5[.]5"


const solution = (str) => {
  return str.replaceAll(".", "[.]");
};

console.log(sol("5.5.5.5.5"));
