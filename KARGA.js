export const KARGA = {

  scan(modules){
    const found = [];

    for(const name in modules){
      if(modules[name]){
        found.push({
          name,
          type: typeof modules[name],
          state: "FOUND"
        });
      }
    }

    return {
      karga: "OK",
      count: found.length,
      modules: found
    };
  }
};
