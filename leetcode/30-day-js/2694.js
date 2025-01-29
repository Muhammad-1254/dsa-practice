class EventEmitter {
  /**
   * @param {string} eventName
   * @param {Function} callback
   * @return {Object}
   */

  events = new Map();

  subscribe(eventName, callback) {
    const id = Symbol();

    if (!this.events.has(eventName)) {
      this.events.set(eventName, new Map());
    }

    this.events.get(eventName).set(id, callback);

    return {
      unsubscribe: () => {
        return this.events.get(eventName)?.delete(id);
      },
    };
  }

  /**
   * @param {string} eventName
   * @param {Array} args
   * @return {Array}
   */
  emit(eventName, args = []) {
    const fns = this.events.get(eventName).values() ?? [];
    return Array.from(fns).map((fn) => fn(...args));
  }
}

const emitter = new EventEmitter();

const e1 = emitter.subscribe("firstEvent", (x) => x + 1);
const e2 = emitter.subscribe("firstEvent", (x) => x + 2);
const e3 = emitter.subscribe("firstEvent", (x) => x + 3);
e2.unsubscribe();
e3.unsubscribe();
console.log(emitter.emit("firstEvent", [5]));
