export function save(result) {
  localStorage.setItem(result.name, JSON.stringify(result));
}

export function load(name) {
  return JSON.parse(localStorage.getItem(name));
}

